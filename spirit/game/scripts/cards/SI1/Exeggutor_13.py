from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import sharpshooter


card = PokemonCardDef(
    guid="9d21a85d-4539-5f7f-9180-34d94424bebe",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1", "Exeggutor"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=103,
    abilities=[
        Attack(
            title="Sharpshooter",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. Flip a number of coins equal to the number of Grass Energy attached to Exeggutor. This attack does 10 damage times the number of heads to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.GRASS: 1},
            effect=sharpshooter,
        ),
    ],
)
