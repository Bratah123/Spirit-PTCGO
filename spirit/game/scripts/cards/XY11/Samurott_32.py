from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import snipe_attack


async def _ultimate_blade(ctx):
    """40; if the damage reduces the opponent's Active to 60 HP or less, it is Knocked Out."""
    d = ctx.opponent_active()
    before = int(d.get_attribute(AttrID.HP) or 0) if d is not None else 0
    await ctx.deal_damage()
    if d is None or d is not ctx.opponent_active():
        return
    after = int(d.get_attribute(AttrID.HP) or 0)
    if 0 < after <= 60 and after < before:
        await ctx.knock_out(d)


card = PokemonCardDef(
    guid="d67ed84e-dc0f-5bce-94bb-685a880b3964",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Samurott.Name",
    display_name="Samurott",
    searchable_by=["Samurott", "Stage 2", "Samurott"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    family_id=501,
    abilities=[
        Attack(
            title="Ultimate Blade",
            game_text="If the damage from this attack reduces your opponent's Active Pok\u00e9mon's HP to 60 or less, that Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_ultimate_blade,
        ),
        Attack(
            title="Pike",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=snipe_attack(30, also_base=True),
        ),
    ],
)