from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import form_change_deoxys, crystal_laser_lock


card = PokemonCardDef(
    guid="3202f893-59ca-55f2-ae0b-971cb0962c04",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys δ",
    searchable_by=["Deoxys δ", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="POP4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Form Change",
            game_text="Once during your turn (before your attack), you may search your deck for another Deoxys and switch it with Deoxys. (Any cards attached to Deoxys, damage counters, Special Conditions, and effects on it are now on the new Pokémon.) If you do, put Deoxys on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Poké-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            shared_once_per_turn="Form Change",
            effect=form_change_deoxys(),
        ),
        Attack(
            title="Crystal Laser",
            game_text="During your next turn, Deoxys's attacks do 40 more damage to the Defending Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=crystal_laser_lock(),
        ),
    ],
)
