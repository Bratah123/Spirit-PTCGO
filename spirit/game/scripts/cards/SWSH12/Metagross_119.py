from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b4117c0-c560-5a3e-a6da-31db879bbac8",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=119,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Emergency Entry",
            game_text="Once during your turn, if you drew this Pok\u00e9mon from your deck at the beginning of your turn and your Bench isn't full, before you put it into your hand, you may put it onto your Bench. If you do, draw 3 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Meteor Mash",
            game_text="During your next turn, this Pok\u00e9mon's Meteor Mash attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)