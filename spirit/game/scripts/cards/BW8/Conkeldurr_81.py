from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CLIENT_SPECIAL_CONDITION_NAMES, SpecialConditions
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.attacks_common import bonus_if


def _has(pokemon, condition):
    return CLIENT_SPECIAL_CONDITION_NAMES[condition] in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


def _burned_or_poisoned(ctx):
    me = ctx.attacker
    return _has(me, SpecialConditions.BURNED) or _has(me, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="d9bac783-f8a3-5516-9d9c-37436c90d6e9",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Conkeldurr.Name",
    display_name="Conkeldurr",
    searchable_by=["Conkeldurr", "Stage 2", "Conkeldurr"],
    subtypes=["Stage 2"],
    collector_number=81,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    family_id=532,
    abilities=[
        Attack(
            title="Facade",
            game_text="If this Pok\u00e9mon is Burned or Poisoned, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_burned_or_poisoned, 60),
        ),
        Attack(
            title="Drain Punch",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=heal_attack(20),
        ),
    ],
)