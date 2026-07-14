from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="2e9bf2ed-ca51-5c17-8f91-a9057b71cedb",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1", "Liepard"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 40 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=40),
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)