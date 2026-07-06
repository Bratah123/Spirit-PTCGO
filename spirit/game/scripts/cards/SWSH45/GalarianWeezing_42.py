from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bceaefbe-6be9-54ab-87a0-675ff554bf50",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianWeezing.Name",
    display_name="Galarian Weezing",
    searchable_by=["Galarian Weezing", "Stage 1", "GalarianWeezing"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SWSH45",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Neutralizing Gas",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Pok\u00e9mon in play have no Abilities, except for Neutralizing Gas.",
            effect=unimplemented,
        ),
        Attack(
            title="Severe Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 4 damage counters instead of 1 on that Pok\u00e9mon during Pok\u00e9mon Checkup.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
    ],
)