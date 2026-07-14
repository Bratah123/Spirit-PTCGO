from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def silent_wing(ctx):
    await ctx.deal_damage()
    await ctx.reveal_hand(of_player=ctx.opponent_id)


card = PokemonCardDef(
    guid="4e924105-d173-5a29-8aab-9ea8e6b0875e",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    display_name="Noctowl",
    searchable_by=["Noctowl", "Stage 1", "Noctowl"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    family_id=163,
    abilities=[
        Attack(
            title="Silent Wing",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=silent_wing,
        ),
        Attack(
            title="Air Slash",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)