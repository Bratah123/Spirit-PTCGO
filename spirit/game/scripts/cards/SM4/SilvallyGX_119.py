from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.attacks_common import damage_per, count_bench
from spirit.game.card_effects.sm4 import gyro_unit_passive


card = PokemonCardDef(
    guid="c4fa85e6-181a-5772-a84c-bc56b3e71f78",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SilvallyGX.Name",
    display_name="Silvally-GX",
    searchable_by=["Silvally-GX", "Stage 1", "GX", "SilvallyGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=119,
    set_code="SM4",
    rarity=Rarities.RareRainbow,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    family_id=772,
    abilities=[
        Ability(
            title="Gyro Unit",
            game_text="Your Basic Pok\u00e9mon in play have no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=gyro_unit_passive,
        ),
        Attack(
            title="Turbo Drive",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=attach_from_discard(predicate=is_basic_energy_card, count=1, target=lambda p: not is_in_active_spot(p), prompt='Choose a basic Energy card to attach to a Benched Pokémon'),
        ),
        Attack(
            title="Rebel-GX",
            game_text="This attack does 50 damage for each of your opponent's Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=damage_per(count_bench('opponent'), 50),
        ),
    ],
)