from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.passives import carrier_pokemon


def _has_cond(p, cond):
    return p is not None and CLIENT_SPECIAL_CONDITION_NAMES[cond] in (p.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


def _from_poisoned(calc, carrier):
    return calc.target is carrier_pokemon(carrier) and _has_cond(calc.attacker, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="7508a80b-3870-5183-adeb-5b04c624dd4b",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name",
    display_name="Toxicroak",
    searchable_by=["Toxicroak", "Stage 1", "Toxicroak"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    family_id=453,
    abilities=[
        Ability(
            title="Poison Enzyme",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Poisoned Pok\u00e9mon.",
            passive=prevent_damage_when(_from_poisoned),
        ),
        Attack(
            title="Poison Jab",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)