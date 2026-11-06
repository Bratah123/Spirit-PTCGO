from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn


card = PokemonCardDef(
    guid="745c4bec-a21f-555a-abe9-75ae0d94f93e",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1", "Machoke"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Machoke's Mega Punch attack's base damage is 80.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=boost_own_next_turn(40, attack_title="Mega Punch"),
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
