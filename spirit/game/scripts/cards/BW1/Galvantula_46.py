from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


async def _leech_life(ctx):
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt)


card = PokemonCardDef(
    guid="680227dc-1f5d-5508-a796-d207a9b58bc2",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula", "Stage 1", "Galvantula"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Attack(
            title="Electroweb",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Leech Life",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_leech_life,
        ),
    ],
)
