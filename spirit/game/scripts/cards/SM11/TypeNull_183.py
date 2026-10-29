from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="02ef285e-c666-507f-95bd-9849220aab21",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    display_name="Type: Null",
    searchable_by=["Type: Null", "Basic", "TypeNull"],
    subtypes=["Basic"],
    collector_number=183,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=772,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Quick Blow",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)