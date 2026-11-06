from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import triple_bone


card = PokemonCardDef(
    guid="42f0aad6-eb05-5635-8d5e-1d0602c70fa3",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak",
    searchable_by=["Marowak", "Stage 1", "Marowak"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Triple Bone",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. Flip 3 coins. This attack does 10 damage times the number of heads to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=triple_bone,
        ),
        Attack(
            title="Bone Rush",
            game_text="Flip a coin until you get tails. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=50),
        ),
    ],
)
