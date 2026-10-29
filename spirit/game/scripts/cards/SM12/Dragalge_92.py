from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import poison_cultivation

card = PokemonCardDef(
    guid="4b82e101-ecf1-5967-b620-1fdf66d5030f",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragalge.Name",
    display_name="Dragalge",
    searchable_by=["Dragalge", "Stage 1", "Dragalge"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    family_id=690,
    abilities=[
        Attack(
            title="Poison Cultivation",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, put 10 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=poison_cultivation,
        ),
        Attack(
            title="Sharp Fin",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
        ),
    ],
)