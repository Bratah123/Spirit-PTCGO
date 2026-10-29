from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="5f1c5c31-05de-52be-8ae6-2ce447489ff0",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Attack(
            title="Reflect",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 40 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=protect_next_turn(reduce=40),
        ),
        Attack(
            title="Psychic Corkscrew",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=feint,
        ),
    ],
)