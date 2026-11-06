from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.content.definitions import def_for


def _named(p, name):
    return getattr(def_for(p.archetype_id), "display_name", None) == name


async def _swarming_sting(ctx):
    """40 times the number of Beedrill you have in play to 1 of the opponent's Pokemon."""
    n = sum(1 for p in ctx.my_pokemon_in_play() if _named(p, "Beedrill"))
    pool = ctx.opponent_pokemon_in_play()
    if not n or not pool:
        return
    t = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, f"Choose a Pokémon to take {40 * n} damage")
    if t is not None:
        await ctx.deal_damage(40 * n, target=t, apply_modifiers=None)


card = PokemonCardDef(
    guid="23b30fff-f5b9-5be0-94e0-00fc539c7c44",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Swarming Sting",
            game_text="This attack does 40 damage times the number of Beedrill you have in play to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=_swarming_sting,
        ),
    ],
)