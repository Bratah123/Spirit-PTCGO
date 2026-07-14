from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, active_is, recoil_attack
from spirit.game.session.effects import is_evolution_pokemon

card = PokemonCardDef(
    guid="b5cc2269-b439-57df-ac29-b9b4826794e5",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braviary.Name",
    display_name="Braviary",
    searchable_by=["Braviary", "Stage 1", "Braviary"],
    subtypes=["Stage 1"],
    collector_number=137,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    family_id=627,
    abilities=[
        Attack(
            title="Valiant Talons",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(active_is(is_evolution_pokemon), 60),
        ),
        Attack(
            title="Brave Bird",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=recoil_attack(50),
        ),
    ],
)