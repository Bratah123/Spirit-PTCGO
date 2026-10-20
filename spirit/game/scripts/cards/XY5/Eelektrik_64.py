from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="1d32ec0a-cceb-5a28-96b9-bf4f745c491d",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    display_name="Eelektrik",
    searchable_by=["Eelektrik", "Stage 1", "Eelektrik"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    family_id=602,
    abilities=[
        ancient_trait('α Recovery'),
        Attack(
            title="Thrash",
            game_text="Flip a coin. If heads, this attack does 20 more damage. If tails, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_damage(bonus=20, require_all=True, tails_self_damage=20),
        ),
    ],
)