from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import retreat_free_when

async def rock_polish(ctx):
    """During your next turn, this Pokémon has no Retreat Cost."""
    from spirit.game.card_effects.passives_common import retreat_free_when
    from spirit.game.session.passives import carrier_pokemon
    ctx.add_passive_through_own_next_turn(
        ctx.attacker,
        retreat_free_when(lambda p, c: p is carrier_pokemon(c)),
    )


card = PokemonCardDef(
    guid="e3dce8e1-3a60-5d48-a096-2faff6b24550",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name",
    display_name="Alolan Geodude",
    searchable_by=["Alolan Geodude", "Basic", "AlolanGeodude"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=74,
    abilities=[
        Attack(
            title="Rock Polish",
            game_text="During your next turn, this Pok\u00e9mon has no Retreat Cost.",
            cost={},
            effect=rock_polish,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)