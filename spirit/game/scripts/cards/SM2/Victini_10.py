from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.session.passives import Passive


class VictoryStarPassive(Passive):
    def offers_attack_coin_reroll(self, player_id, carrier):
        return player_id == carrier.owning_player_id


card = PokemonCardDef(
    guid="0f6750fc-1d1a-5a64-a013-bbbeb7a85550",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Ability(
            title="Victory Star",
            game_text="Once during your turn, after you flip any coins for an attack, you may ignore all results of those coin flips and begin flipping those coins again. You can't use more than 1 Victory Star Ability each turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=VictoryStarPassive(),
            effect=None,
        ),
        Attack(
            title="V-Flame",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)