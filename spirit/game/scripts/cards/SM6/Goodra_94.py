from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.sm6 import hydration
from spirit.game.data_utils import Triggers

def _healed_this_turn(ctx):
    return ctx.attacker.entity_id in ctx.session.turn_state.healed_entities

card = PokemonCardDef(
    guid="c07a378f-e7bb-5dde-90e3-de9e09e1ebc1",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name",
    display_name="Goodra",
    searchable_by=["Goodra", "Stage 2", "Goodra"],
    subtypes=["Stage 2"],
    collector_number=94,
    set_code="SM6",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    family_id=704,
    abilities=[
        Ability(
            title="Hydration",
            game_text="Whenever you attach a Water Energy card from your hand to this Pok\u00e9mon, heal 20 damage from it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=hydration,
        ),
        Attack(
            title="Soaking Horn",
            game_text="If this Pok\u00e9mon was healed during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_healed_this_turn, 80),
        ),
    ],
)
