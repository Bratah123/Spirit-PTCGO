from spirit.game.data_utils import VUnionPokemonDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import UnfazedFatPassive
from spirit.game.card_effects.support_common import attach_from_discard, heal_attack
from spirit.game.card_effects.trainers import is_psychic_energy_card


async def psysplosion(ctx):
    """Put 16 damage counters on your opponent's Pokemon in any way you like."""
    await ctx.place_damage_counters(16, ctx.opponent_pokemon_in_play())


card = VUnionPokemonDef(
    guid="16d7d8db-c163-5c47-80c9-98aa71d81b81",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoVUNION.Name",
    display_name="Mewtwo V-UNION",
    searchable_by=["Mewtwo V-UNION", "V-UNION", "MewtwoVUNION"],
    collector_number=159,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[
        Ability(
            title="Photon Barrier",
            game_text="Prevent all effects of attacks from your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            passive=UnfazedFatPassive(),
        ),
        Attack(
            title="Union Gain",
            game_text="Attach up to 2 Psychic Energy cards from your discard pile to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(predicate=is_psychic_energy_card, count=2, minimum=0),
        ),
        Attack(
            title="Super Regeneration",
            game_text="Heal 200 damage from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=heal_attack(200),
        ),
        Attack(
            title="Psysplosion",
            game_text="Put 16 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=psysplosion,
        ),
        Attack(
            title="Final Burn",
            cost={PokemonTypes.PSYCHIC: 3, PokemonTypes.COLORLESS: 1},
            damage=300,
        ),
    ],
)
