from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn
from spirit.game.card_effects.support_common import draw_attack


card = PokemonCardDef(
    guid="6a332f09-c9e7-5508-b09f-b4d343c4506a",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Attack(
            title="Close Encounter",
            game_text="If you go first, you can use this attack on your first turn. Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            usable_first_turn=True,
            effect=draw_attack(2),
        ),
        Attack(
            title="Overdrive Smash",
            game_text="During your next turn, this Pok\u00e9mon's Overdrive Smash attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=boost_own_next_turn(60, attack_title='Overdrive Smash'),
        ),
    ],
)