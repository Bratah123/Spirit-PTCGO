from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.session.passives import Passive


class RoadblockPassive(Passive):
    def bench_capacity(self, player_id, carrier):
        if player_id == carrier.owning_player_id:
            return None
        return 4


card = PokemonCardDef(
    guid="6a62e4e1-6bea-5a0d-8f5f-b53ede491e6c",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Ability(
            title="Roadblock",
            game_text="Your opponent can't have more than 4 Benched Pok\u00e9mon. If they have 5 or more Benched Pok\u00e9mon, they discard Benched Pok\u00e9mon until they have 4 Pok\u00e9mon on the Bench. If more than one effect changes the number of Benched Pok\u00e9mon allowed, use the smaller number.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=RoadblockPassive(),
            effect=None,
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)