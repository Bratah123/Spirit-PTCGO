from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _dedenne_dede_short_last_turn(ctx):
    for pokemon in ctx.my_pokemon_in_play():
        card_def = def_for(pokemon.archetype_id)
        if card_def and card_def.display_name == "Dedenne" and \
                ctx.attack_used_last_turn(title="Dede-Short", entity=pokemon):
            return True
    return False


card = PokemonCardDef(
    guid="caad81a2-cd85-5271-b05b-d83f3649e624",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Pika Strike",
            game_text="If 1 of your Dedenne used Dede-Short during your last turn, this attack does 180 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_dedenne_dede_short_last_turn, 180),
        ),
    ],
)