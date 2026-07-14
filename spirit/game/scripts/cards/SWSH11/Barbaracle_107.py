from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class LostBlockPassive(Passive):
    def prize_destination(self, pokemon, ctx, carrier):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return "lostZone"
        return None


card = PokemonCardDef(
    guid="c19dbbcf-dd24-59a0-b223-b8a3ad95f377",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barbaracle.Name",
    display_name="Barbaracle",
    searchable_by=["Barbaracle", "Stage 1", "Barbaracle"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    family_id=688,
    abilities=[
        Ability(
            title="Lost Block",
            game_text="Your opponent puts any Prize cards they would take in the Lost Zone instead of into their hand.",
            passive=LostBlockPassive(),
        ),
        Attack(
            title="Dynamic Chop",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
