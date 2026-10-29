from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import rock_crush
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def _grand_echo(ctx):
    """Heal all damage from all of your Pokemon."""
    for p in ctx.my_pokemon_in_play():
        await ctx.heal(ctx.max_hp(p), p)


card = PokemonCardDef(
    guid="b5a90365-8e0e-5edc-8e85-95dd4f6d333a",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PrimarinaGX.Name",
    display_name="Primarina-GX",
    searchable_by=["Primarina-GX", "Stage 2", "GX", "PrimarinaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=42,
    set_code="SM1",
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    family_id=728,
    abilities=[
        Attack(
            title="Bubble Beat",
            game_text="This attack does 20 more damage times the amount of Water Energy attached to your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy('mine', energy_type=PokemonTypes.WATER), 20, base=10),
        ),
        Attack(
            title="Roaring Seas",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=rock_crush,
        ),
        Attack(
            title="Grand Echo-GX",
            game_text="Heal all damage from all of your Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_grand_echo,
        ),
    ],
)