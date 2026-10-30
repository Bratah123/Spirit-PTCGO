from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    AttrID, PokemonTypes, PokemonStage, Rarities, AbilityTypes,
    SpecialConditions,
)
from spirit.game.card_effects.attacks_common import active_is, bonus_if
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.session.effects import is_evolution_pokemon


def _is_seviper(pokemon):
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Seviper"


card = PokemonCardDef(
    guid="f48a8027-545f-551a-9be1-abaad3b8988b",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name",
    display_name="Zangoose",
    searchable_by=["Zangoose", "Basic", "Zangoose"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Ability(
            title="Poison Resistance",
            game_text="Zangoose can't be Poisoned.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=condition_immunity_passive(SpecialConditions.POISONED),
        ),
        Attack(
            title="Target Slash",
            game_text="If the Defending Pok\u00e9mon is Seviper, this attack does 10 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(active_is(_is_seviper), 30),
        ),
        Attack(
            title="Super Slash",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=bonus_if(active_is(is_evolution_pokemon), 30),
        ),
    ],
)
