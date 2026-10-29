from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import unnerve_passive
from spirit.game.card_effects.support_common import recover_from_discard

card = PokemonCardDef(
    guid="a7912887-0c65-5e2b-a970-db7dd46e39e2",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula", "Stage 1", "Galvantula"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Ability(
            title="Unnerve",
            game_text="Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=unnerve_passive,
        ),
        Attack(
            title="Spider Thread",
            game_text="Put a card from your discard pile into your hand.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
            effect=recover_from_discard(count=1, minimum=1, reveal=False, to='hand'),
        ),
    ],
)