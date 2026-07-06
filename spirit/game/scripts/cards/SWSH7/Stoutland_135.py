from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb599bc2-319e-5fab-98f4-f7456439d764",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2", "Stoutland"],
    subtypes=["Stage 2"],
    collector_number=135,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Ability(
            title="Intimidating Fang",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Active Pok\u00e9mon's attacks do 30 less damage (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)