from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage
from spirit.game.card_effects.ex import attach_as_many_from_hand
from spirit.game.card_effects.trainers import is_water_energy_card


card = PokemonCardDef(
    guid="c89eb069-67ed-5ffb-b14a-c08d6e22d755",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Attack(
            title="Drizzle",
            game_text="If you have Water Energy cards in your hand, attach as many Water Energy cards as you like to any of your Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_as_many_from_hand(
                is_water_energy_card, target="active",
                prompt="Choose Water Energy cards to attach.",
            ),
        ),
        Attack(
            title="Max Bubbles",
            game_text="Flip a coin for each Energy attached to all of your Active Pok\u00e9mon. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy("my_active"), per_heads=30),
        ),
    ],
)
