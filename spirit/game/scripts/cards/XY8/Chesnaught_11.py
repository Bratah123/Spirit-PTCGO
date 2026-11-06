from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="d87f5e41-e39f-5f01-9e76-cf6d5e25028d",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chesnaught.Name",
    display_name="Chesnaught",
    searchable_by=["Chesnaught", "Stage 2", "Chesnaught"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilladin.Name",
    family_id=650,
    abilities=[
        Attack(
            title="Spike Lariat",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(has_damage(), 60),
        ),
        Attack(
            title="Adamantine Press",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=protect_next_turn(reduce=20),
        ),
    ],
)