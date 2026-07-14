from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import is_pokemon_gx


async def big_sparking(ctx):
    """50 to each Pokemon V and Pokemon-GX, both sides; no W/R on the Bench."""
    opponent_active = ctx.opponent_active()
    targets = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    for pokemon in targets:
        if is_pokemon_v(pokemon.archetype_id) or is_pokemon_gx(pokemon.archetype_id):
            await ctx.deal_damage(
                50, target=pokemon, apply_modifiers=(pokemon is opponent_active)
            )


card = PokemonCardDef(
    guid="ab225dfa-785f-5a87-b866-d1ea7cccf07d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Big Sparking",
            game_text="This attack does 50 damage to each Pok\u00e9mon V and Pok\u00e9mon-GX (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=big_sparking,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)