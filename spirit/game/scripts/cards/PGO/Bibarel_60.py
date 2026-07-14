from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import Passive, carrier_pokemon, is_in_active_spot


class ReassuringDamPassive(Passive):
    def blocks_discard(self, card, carrier):
        pokemon = carrier_pokemon(carrier)
        if pokemon is None or is_in_active_spot(pokemon):
            return False
        if card.owning_player_id != pokemon.owning_player_id:
            return False
        parent = getattr(card, "parent", None)
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "deck"


card = PokemonCardDef(
    guid="b836a69f-4559-5d3c-aba3-bdd242fdcf57",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name",
    display_name="Bibarel",
    searchable_by=["Bibarel", "Stage 1", "Bibarel"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="PGO",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    family_id=399,
    abilities=[
        Ability(
            title="Reassuring Dam",
            game_text="As long as this Pokémon is on your Bench, cards in your deck can't be discarded by effects of your opponent's attacks, Abilities, Item cards, or Supporter cards.",
            passive=ReassuringDamPassive(),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
