from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import attach_hand_energy
from spirit.game.card_effects.trainers import is_grass_energy_card


card = PokemonCardDef(
    guid="d46ed157-78ac-5743-83e7-cb8ab3263108",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    display_name="Weepinbell",
    searchable_by=["Weepinbell", "Stage 1", "Weepinbell"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Growth",
            game_text="Attach up to 2 Grass Energy cards from your hand to Weepinbell.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_hand_energy(
                count=2, predicate=is_grass_energy_card, minimum=0),
        ),
        Attack(
            title="Double Razor Leaf",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
    ],
)
