from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="874507d4-bbe2-5e61-b083-3a8eaea2cab2",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=36,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Attack(
            title="Bubble",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Double Cannon",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=40),
        ),
    ],
)
