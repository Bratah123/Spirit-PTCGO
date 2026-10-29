from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="f02df417-b6a9-519a-9e47-38fa518110ca",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic", "Turtonator"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Steam Artillery",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)