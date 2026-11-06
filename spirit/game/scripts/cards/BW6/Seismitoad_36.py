from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="d2227ac5-b672-54fa-a0e9-e0e819a95c99",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=36,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Echoed Voice",
            game_text="During your next turn, this Pok\u00e9mon's Echoed Voice attack does 50 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=boost_own_next_turn(50, attack_title='Echoed Voice'),
        ),
        Attack(
            title="Drain Punch",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=heal_attack(20),
        ),
    ],
)