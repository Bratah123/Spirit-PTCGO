from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _healed_this_turn(ctx):
    return ctx.attacker.entity_id in ctx.session.turn_state.healed_entities


card = PokemonCardDef(
    guid="7aca8ca1-5bee-5796-a864-844d62096c66",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirV.Name",
    display_name="Gardevoir V",
    searchable_by=["Gardevoir V", "Basic", "V", "GardevoirV"],
    subtypes=["Basic", "V"],
    collector_number=16,
    set_code="SWSH35",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=282,
    abilities=[
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Swelling Pulse",
            game_text="If this Pok\u00e9mon was healed during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=bonus_if(_healed_this_turn, 80),
        ),
    ],
)