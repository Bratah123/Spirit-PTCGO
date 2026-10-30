from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import discard_energy_then_condition
from spirit.game.attributes import SpecialConditions

card = PokemonCardDef(
    guid="46b201c2-5b7e-543f-b6f8-1d2cc782ea46",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    display_name="Grimer",
    searchable_by=["Grimer", "Basic", "Grimer"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="EX3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=88,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Poison Spurt",
            game_text="Discard a Grass Energy card attached to Grimer. The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=discard_energy_then_condition(PokemonTypes.GRASS, SpecialConditions.POISONED),
        ),
    ],
)