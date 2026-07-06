from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9f4f4d4d-f28f-532a-a1da-09ec3186a1a5",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solgaleo.Name",
    display_name="Solgaleo",
    searchable_by=["Solgaleo", "Stage 2", "Solgaleo"],
    subtypes=["Stage 2"],
    collector_number=21,
    set_code="CEL25",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=789,
    abilities=[
        Ability(
            title="Rush In",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, you may switch it with your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Solar Geyser",
            game_text="Attach up to 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)