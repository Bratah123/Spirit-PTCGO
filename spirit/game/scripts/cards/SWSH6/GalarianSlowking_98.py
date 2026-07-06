from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d944645a-0420-5347-b863-d5f6a19e1208",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowking.Name",
    display_name="Galarian Slowking",
    searchable_by=["Galarian Slowking", "Stage 1", "GalarianSlowking"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Mysterious Potion",
            game_text="Once during your turn, you may choose 1 of your Pok\u00e9mon and flip a coin. If heads, heal 90 damage from that Pok\u00e9mon. If tails, put 3 damage counters on that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Spray Fluid",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)