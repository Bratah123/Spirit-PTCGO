from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="dd660638-140a-5674-b35d-f553eddc5a37",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    display_name="Shieldon",
    searchable_by=["Shieldon", "Restored", "Shieldon"],
    subtypes=["Restored"],
    collector_number=69,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArmorFossilShieldon.Name",
    family_id=410,
    abilities=[
        Attack(
            title="Rock Head",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)