from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="4f79cf32-4466-5cf1-9023-16e5bde404a2",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic", "Sigilyph"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=561,
    abilities=[
        Attack(
            title="Reflect",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 40 (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=protect_next_turn(reduce=40),
        ),
        Attack(
            title="Telekinesis",
            game_text="Does 50 damage to 1 of your opponent's Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(50, pool="any", apply_modifiers=False),
        ),
    ],
)
