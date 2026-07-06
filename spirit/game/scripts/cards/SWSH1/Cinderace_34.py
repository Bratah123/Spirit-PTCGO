from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9a908f80-98fe-5529-aeb7-aa5aaf67fdbe",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinderace.Name",
    display_name="Cinderace",
    searchable_by=["Cinderace", "Stage 2", "Cinderace"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    family_id=813,
    abilities=[
        Ability(
            title="Libero",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may attach up to 2 Fire Energy cards from your discard pile to it.",
            effect=unimplemented,
        ),
        Attack(
            title="Flare Striker",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=unimplemented,
        ),
    ],
)