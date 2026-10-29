from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.gum import pantomime

card = PokemonCardDef(
    guid="c4252959-5d3f-54f5-87e0-a1c87270836e",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="GUM",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Ability(
            title="Pantomime",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may switch 1 of your face-down Prize cards with the top card of your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_PLAY,
            effect=pantomime,
        ),
        Attack(
            title="Juggling",
            game_text="Flip 4 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=20),
        ),
    ],
)
