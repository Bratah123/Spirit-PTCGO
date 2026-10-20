from spirit.game.data_utils import StadiumCardDef, Attack, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive
from spirit.game.models.board import PokemonEntity


class _ShrineOfMemories(Passive):
    """Each evolved Pokemon can use any attack from its previous Evolutions."""
    def granted_attacks(self, board, pokemon, carrier):
        out, stack = [], [c for c in pokemon.children if isinstance(c, PokemonEntity)]
        while stack:
            pre = stack.pop()
            for a in getattr(def_for(pre.archetype_id), "abilities", None) or []:
                if isinstance(a, Attack):
                    out.append(a)
            stack.extend(c for c in pre.children if isinstance(c, PokemonEntity))
        return out


card = StadiumCardDef(
    guid="23a9102a-c29c-510f-a38e-8d8488f7a361",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofMemories.Name",
    display_name="Shrine of Memories",
    searchable_by=["Shrine of Memories", "Stadium"],
    subtypes=["Stadium"],
    collector_number=139,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=_ShrineOfMemories()
)
