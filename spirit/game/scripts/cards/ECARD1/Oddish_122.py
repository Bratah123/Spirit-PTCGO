from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="c377a29b-760c-5108-a623-a1aada980295",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    display_name="Oddish",
    searchable_by=["Oddish", "Basic", "Oddish"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=43,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Sleep Seed",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
