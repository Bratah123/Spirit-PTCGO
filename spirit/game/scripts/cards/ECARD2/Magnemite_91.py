from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import ConductiveBodyPassive


card = PokemonCardDef(
    guid="10ff4330-f434-522c-a68f-dc52fb34f170",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=81,
    abilities=[
        Ability(
            title="Conductive Body",
            game_text="You pay Colorless less to retreat Magnemite for each Magnemite on your Bench.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=ConductiveBodyPassive(),
        ),
        Attack(
            title="Magnetic Bomb",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage. If tails, Magnemite does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_damage(bonus=10, require_all=True, tails_self_damage=10),
        ),
    ],
)
