from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.session.passives import Passive


class MentalShroudPassive(Passive):
    """If Uxie and Azelf are also in play, your Pokemon have no Weakness."""

    def modify_weakness(self, calc, carrier):
        if calc.target.owning_player_id != carrier.owning_player_id:
            return
        present = {
            p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
            for p in calc.board.pokemon_in_play(carrier.owning_player_id)
        }
        if {"Uxie", "Azelf"} <= present:
            calc.weakness_applies = False


card = PokemonCardDef(
    guid="13051f75-00ec-5c2a-ab40-be71e78d58b1",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name",
    display_name="Mesprit",
    searchable_by=["Mesprit", "Basic", "Mesprit"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=481,
    abilities=[
        Ability(
            title="Mental Shroud",
            game_text="If you have Uxie and Azelf in play, each of your Pok\u00e9mon has no Weakness.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=MentalShroudPassive(),
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)