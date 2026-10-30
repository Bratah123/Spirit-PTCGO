from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import clamping_jaw


card = PokemonCardDef(
    guid="05744dbb-2c02-5473-a601-348f869df2b3",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCroconaw.Name",
    display_name="Dark Croconaw",
    searchable_by=["Dark Croconaw", "Stage 1", "DarkCroconaw"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Clamping Jaw",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn. If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing. (Benching either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=clamping_jaw,
        ),
    ],
)
