from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.models.board import BoardState
from spirit.game.session.effects import is_special_energy


def _skyscraper_pred(calc, carrier):
    if calc.target is not carrier:
        return False
    attacker = calc.attacker
    return attacker is not None and any(
        is_special_energy(e) for e in BoardState.attached_energies(attacker)
    )


async def g_max_pulverization(ctx):
    await ctx.deal_damage(ignore_target_effects=True)


card = PokemonCardDef(
    guid="5699247a-db0f-5428-9ac4-b9fde390dd1c",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DuraludonVMAX.Name",
    display_name="Duraludon VMAX",
    searchable_by=["Duraludon VMAX", "VMAX", "Single Strike", "DuraludonVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=219,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DuraludonV.Name",
    family_id=884,
    abilities=[
        Ability(
            title="Skyscraper",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon that have Special Energy attached.",
            passive=prevent_damage_when(_skyscraper_pred),
        ),
        Attack(
            title="G-Max Pulverization",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 2},
            damage=220,
            effect=g_max_pulverization,
        ),
    ],
)