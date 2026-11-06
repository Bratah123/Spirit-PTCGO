from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import earth_rift, iron_smash


card = PokemonCardDef(
    guid="a081662b-c889-5784-8bf5-d9b1b6b5e939",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1", "Steelix"],
    subtypes=["Stage 1"],
    collector_number=173,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Attack(
            title="Earth Rift",
            game_text="This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.) Then, flip a coin. If tails, this attack can't be used during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=earth_rift,
        ),
        Attack(
            title="Iron Smash",
            game_text="Flip 2 coins. If both are heads, this attack does 50 damage plus 20 more damage. If both are tails, this attack does nothing. If 1 is heads and 1 is tails, this attack just does 50 damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=iron_smash,
        ),
    ],
)
