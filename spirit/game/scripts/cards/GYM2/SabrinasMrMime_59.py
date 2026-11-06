from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import magic_darts


card = PokemonCardDef(
    guid="31d2782e-64ad-563a-932f-64261142c5cf",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasMrMime.Name",
    display_name="Sabrina's Mr. Mime",
    searchable_by=["Sabrina's Mr. Mime", "Basic", "SabrinasMrMime"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Attack(
            title="Magic Darts",
            game_text="Choose 1 of your opponent's Pok\u00e9mon and flip 3 coins. This attack does 10 damage times the number of heads to that Pok\u00e9mon. Don't apply Weakness and Resistance for this attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=magic_darts,
        ),
    ],
)
