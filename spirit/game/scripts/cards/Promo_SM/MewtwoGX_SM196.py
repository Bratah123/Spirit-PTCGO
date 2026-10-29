from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, condition_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.smp import psychic_nova_gx


card = PokemonCardDef(
    guid="7a4af434-c6b0-56aa-ba20-f767a02a4688",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoGX.Name",
    display_name="Mewtwo-GX",
    searchable_by=["Mewtwo-GX", "Basic", "GX", "MewtwoGX"],
    subtypes=["Basic", "GX"],
    collector_number=196,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Telekinesis",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(50, pool='any', apply_modifiers=False),
        ),
        Attack(
            title="Reigning Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Psychic Nova-GX",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=psychic_nova_gx,
        ),
    ],
)